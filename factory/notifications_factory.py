from factory.base import Base

from factory.base import create_payload


class NotificationsFactory(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.notifications_path = "/v1/notifications"

    def get_notifications(self):
        return self.get(self.notifications_path, '', self.content_type)

    def set_notification_read_status(self, notification_ref: str,
                                     status: bool, timestamp: float):
        payload = create_payload({
            'notification_ref': notification_ref,
            'status': status,
            'timestamp': timestamp,
        })
        return self.put(self.notifications_path, payload, self.content_type)
