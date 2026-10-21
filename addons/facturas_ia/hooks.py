def post_init_hook(env):
    pendiente = getattr(env.registry, "_auto_install_template", None)
    if pendiente:
        def cargar_plan_y_configurar(env):
            pendiente(env)
            _configurar_companias(env)
        env.registry._auto_install_template = cargar_plan_y_configurar
    else:
        _configurar_companias(env)


def _configurar_companias(env):
    pen = env.ref("base.PEN")
    if not pen.active:
        pen.active = True

    for company in env["res.company"].search([]):
        if not company.chart_template:
            env["account.chart.template"].try_loading("generic_coa", company, install_demo=False)

        sin_movimientos = not env["account.move.line"].search_count([("company_id", "=", company.id)], limit=1)
        if company.currency_id != pen and sin_movimientos:
            company.currency_id = pen

        Tax = env["account.tax"].with_company(company)
        exists = Tax.search([
            ("company_id", "=", company.id),
            ("type_tax_use", "=", "purchase"),
            ("amount_type", "=", "percent"),
            ("amount", "=", 18),
            ("price_include", "=", False),
        ], limit=1)
        if exists:
            continue

        group = env["account.tax.group"].search([("company_id", "=", company.id), ("name", "=", "IGV")], limit=1)
        if not group:
            group = env["account.tax.group"].create({"name": "IGV", "company_id": company.id})

        Tax.create({
            "name": "IGV 18% Compras",
            "description": "IGV 18%",
            "type_tax_use": "purchase",
            "amount_type": "percent",
            "amount": 18,
            "company_id": company.id,
            "tax_group_id": group.id,
        })
