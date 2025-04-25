class App:
    def __init__(self):
        self.routes = {"GET": {}, "POST": {}}
        print("App created!")

    def get(self, path):
        def decorator(func):
            self.routes["GET"][path] = func
            return func
        return decorator

    def post(self, path):
        def decorator(func):
            self.routes["POST"][path] = func
            return func
        return decorator

    def run(self):
        print("App is running!") 
        for method, routes in self.routes.items():
            for path, view in routes.items():
                print(f"{method} route registered: {path} -> {view.__name__}")
def serve():
    print("Serving your app...")
    app.run()