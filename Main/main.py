import Functions.hotspot as hotspot
import Functions.portal as portal
import threading

hotspot.start_hotspot()
portal.restart_dnsmasq
portal.setup_portal()

portal_thread = threading.Thread(
    target=portal.create_portal
)

portal_thread.start()
portal_thread.join()