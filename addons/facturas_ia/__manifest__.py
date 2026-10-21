{
    "name": "Facturas de proveedor: importación automática",
    "version": "18.0.1.0.0",
    "summary": "Registro y trazabilidad de facturas de proveedor importadas desde n8n",
    "category": "Accounting",
    "author": "Diego Rivas Revilla",
    "website": "https://www.diegorivasrevilla.dev",
    "license": "LGPL-3",
    "depends": ["account", "mail"],
    "data": ["views/account_move_views.xml"],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
