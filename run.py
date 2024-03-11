from Chaoxing import Chaoxing
import os

# 你的Cookie信息
# 具体说明看文档
# cookies = ""
cookies = os.environ.get("source=""; lv=3; fid=2948; _uid=194215558; uf=da0883eb5260151e6c3cc7b779606e183064e682fd8107c36954d84cce89e736e9b32d2f65466222a35de0c69402498a913b662843f1f4ad6d92e371d7fdf6444a1534c27620f1ded8a8d0ca21d204ebeea6be31981211d28a9627d218de4acc8f79e26ba3ab2f5b; _d=1709712086629; UID=194215558; vc=220F7C3A83A0F8BB655C7F367713EAF4; vc2=C59E611DF73CACE6A5AAEBE552A7948D; vc3=Uv6koAsqVzE3marw7OLX%2BPpc9%2F%2FLlRUCD9%2BZirMjc%2FELWZQxoNe08t%2BQ0Ey4Ka96wYMhSFXKrueKj4qF6lAz0WlTa4%2F6jZfzuIkCLDfiTcR51ubW7YCIb4nqEKx95pqV%2B3SaisOFICe%2FvK%2BX%2F4rbf4thgNnp%2BPINW%2Fjm7MSNQtA%3D160c699f2db01aff42c4960a9eb8cec2; cx_p_token=16f717d3c4cd87354e585b2f061d6bf9; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxOTQyMTU1NTgiLCJsb2dpblRpbWUiOjE3MDk3MTIwODY2MzAsImV4cCI6MTcxMDMxNjg4Nn0.x3m1Ugn3t0M4JSRlh68y2Orn4Lu1ZhluvfK3wLLGBOs; xxtenc=9df84b675d879806a08bb9a9f6f7a928; DSSTASH_LOG=C_38-UN_1820-US_194215558-T_1709712086631; spaceFid=2948; spaceRoleId=""; route=6c7e83002ce2cc0e78a680d806381539; k8s=1710142054.451.88.58073; jrose=2C49640F671AC1DF2C23DB7BD5083FAF.mooc-4173515402-kzjk5")
# ClassID
# classid = "39007569"
classid = os.environ.get("94978087")
# CourseID
# courseid = "208436724"
courseid = os.environ.get("241759071")
# 请求间隔时间,根据需要更改,单位:秒
# sleep_time = 0.5
sleep_time = float(os.environ.get("0.1"))
# 程序总执行时长,单位:分钟
# pass_time = 10
pass_time = float(os.environ.get("1000000"))
# 下面无需修改
cx = Chaoxing(cookies, classid, courseid, sleep_time, pass_time)
cx.run()
