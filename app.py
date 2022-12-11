
from routing import app, set_server
# ---------------------------------------------------------------------------- #
#                                  FINAL CODE                                  #
# ---------------------------------------------------------------------------- #
# ----------------------- Mounting server up and ready ----------------------- #

# Sets and Mounts server ( for both commands )
# - using `flask run`
# - using `python app.py`
set_server()
if __name__ == '__main__':
	app.run(debug=True)
