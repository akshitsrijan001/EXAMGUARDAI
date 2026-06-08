import pygetwindow as gw
import winsound
import time
import pyautogui
import os


class TabSwitchDetector:

    def __init__(self):

        self.allowed_titles = [
            "ExamGuard AI Monitor",
            "Visual Studio Code"
        ]

        self.violation_logged = False
        self.switch_start_time = None

        os.makedirs(
            "backend/evidence/tab_switch",
            exist_ok=True
        )

    def check_window_focus(self):

        try:

            active_window = gw.getActiveWindow()

            if active_window is None:
                return False

            title = active_window.title

            allowed = any(
                allowed.lower() in title.lower()
                for allowed in self.allowed_titles
            )

            if not allowed:

                if self.switch_start_time is None:

                    self.switch_start_time = time.time()

                    print(
                        f"[INFO] Window changed -> {title}"
                    )

                    return False

                elapsed = (
                    time.time()
                    - self.switch_start_time
                )

                if elapsed >= 3:

                    if not self.violation_logged:

                        timestamp = time.strftime(
                            "%Y%m%d_%H%M%S"
                        )

                        filename = (
                            "backend/evidence/tab_switch/"
                            f"tab_switch_{timestamp}.png"
                        )

                        screenshot = (
                            pyautogui.screenshot()
                        )

                        screenshot.save(
                            filename
                        )

                        winsound.Beep(
                            1000,
                            500
                        )

                        with open(
                            "backend/evidence/violation_log.txt",
                            "a"
                        ) as log:

                            log.write(
                                f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                                "VIOLATION: Tab Switch Detected\n"
                            )

                            log.write(
                                f"File: {filename}\n"
                            )

                            log.write(
                                "Severity: High\n"
                            )

                            log.write(
                                "Status: Logged\n\n"
                            )

                        print(
                            f"[ALERT] Tab Switch -> {title}"
                        )
                        self.violation_logged = True
                        return "VIOLATION"
                        

                    return False

                return False

            self.switch_start_time = None
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