# Odoo.Docker

Review van het opensource pakket Odoo

# Active 
-   export of database
# To Do

-   upgrade to Odoo 17.0


# bash restore
 docker exec -i 202403-odoo-db-1  pg_restore -U odoo -d postgres --clean --no-owner < odoo_2026-03-19_11-18.dump