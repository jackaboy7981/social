# auth_interface.py
# Consumer-side boundary: where auth's OWN service layer reaches out to pull
# data it needs from OTHER modules. auth_service imports from here instead of
# importing another module's services/data_provider directly.
