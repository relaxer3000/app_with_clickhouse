from ch_ocm.repository import CHDBIni
from ch_ocm.user_repository import UserCHRepo
from config.settings import settings


db_name = "app_db"
url = settings.ch_url + db_name
ch_ini = CHDBIni(settings.ch_url)
ocm = UserCHRepo(url)
