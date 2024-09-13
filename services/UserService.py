from database.JdbcDataSource import JdbcDataSource
from services.JDBCRepository import JDBCRepository


class UserService(JDBCRepository):

    def __init__(self, jdbcDataSource: JdbcDataSource) -> None:
        super().__init__(entity_name="employee", id="id", jdbcDataSource=jdbcDataSource)


