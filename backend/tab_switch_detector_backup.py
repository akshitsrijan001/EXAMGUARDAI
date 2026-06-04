import pygetwindow as gw
import winsound
import time


class TabSwitchDetector:

    def __init__(self):

        self.allowed_titles = [
            "ExamGuard AI Monitor",
            "Visual Studio Code"
        ]

        self.violation_logged = False

    def check_window_focus(self):

        try:

            active_window = gw.getActiveWindow()

            if active_window is None:
                return False

            title = active_window.title

            if not any(
                allowed.lower() in title.lower()
                for allowed in self.allowed_titles
            ):

                if not self.violation_logged:

                    print(
                        f"[ALERT] Window Focus Lost -> {title}"
                    )

                    winsound.Beep(1000, 500)

                    self.violation_logged = True

                return True

            self.violation_logged = False
            return False

        except Exception as e:

            print(
                f"Window Detection Error: {e}"
            )

            return False


if __name__ == "__main__":

    detector = TabSwitchDetector()

    print(
        "Monitoring Active Window..."
    )

    while True:

        detector.check_window_focus()

        time.sleep(1)