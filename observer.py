import weakref


class Observable:
    def __init__(self):
        self._observers = weakref.WeakSet()

    def register_observer(self, obs):
        self._observers.add(obs)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, observable):
        observable.register_observer(self) 

    def notify(self, observable, *args, **kwargs):
        print("Got", args, kwargs, "From", observable)


subject = Observable()
observer = Observer(subject)
subject.notify_observers("test", kw="python")

del observer
print("After del")
subject.notify_observers("test", kw="python")
