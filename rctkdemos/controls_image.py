from rctkdemos.demos import serve_demo, standalone
from rctk.widgets import Image, Button
from rctk.resourceregistry import addResource, FileResource

class Demo(object):
    title = "Image"
    description = "Demonstrates the Image control"

    def build(self, tk, parent):
        self.running = False

        resources = [ 
            addResource(FileResource("resources/nyancat-%d.png" % i,
                                     name="nyancat-%d" % i,
                                     type="image/png"))
            for i in range(0, 12)]
        
        img = Image(tk, resource=resources[0])
        button = Button(tk, "Start")
        parent.append(img)
        parent.append(button)

        def update_image(i):
            if self.running:
                img.resource = resources[i]
                tk.set_timer(lambda e: update_image((i+1) % 12), 250)

        def startstop(e):
            button.text = self.running and "Start" or "Stop"
            self.running = not self.running
            update_image(0)

        button.click = startstop

Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

