from strawberry.extensions import Extension

from db.database import db_session


class dbSessionExtension(Extension):
    def on_request_start(self):
        self.execution_context.context["db_session"] = db_session()

    def on_request_end(self):
        self.execution_context.context["db_session"].close()
