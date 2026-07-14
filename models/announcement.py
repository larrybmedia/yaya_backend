from datetime import datetime
from extensions import db


class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    image_filename = db.Column(db.String(255))

    video_url = db.Column(db.String(255))

    admin_id = db.Column(db.Integer, db.ForeignKey("admins.id"))

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
