import Functions.hotspot as hotspot
import Functions.portal as portal
import threading

hotspot.start_hotspot()

portal_thread = threading.Thread(
    target=portal.create_portal,
    daemon=True
)

portal_thread.start()