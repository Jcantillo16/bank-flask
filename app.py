import os
from src import create_app

port = os.getenv('PORT', 5000)
app = create_app(config_name='dev')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
