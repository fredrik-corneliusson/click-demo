from click_web import create_click_web_app
import demo

app = create_click_web_app(demo, demo.cli)