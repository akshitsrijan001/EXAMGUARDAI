"""
Tab Switch Module
Monitors and detects tab switching events during exam sessions
"""

import time
from typing import List, Dict


class TabSwitch:
    """Monitors tab switch events during exam"""
    
    def __init__(self):
        self.tab_switches = []
        self.start_time = None
        
    def log_tab_switch(self, timestamp: float = None):
        """Log a tab switch event"""
        if timestamp is None:
            timestamp = time.time()
        self.tab_switches.append({
            'time': timestamp,
            'detected_at': time.time()
        })
    
    def get_tab_switches(self) -> List[Dict]:
        """Get all recorded tab switches"""
        return self.tab_switches
    
    def reset(self):
        """Reset tab switch log"""
        self.tab_switches = []
    
    def get_switch_count(self) -> int:
        """Get total number of tab switches"""
        return len(self.tab_switches)


if __name__ == "__main__":
    tab_monitor = TabSwitch()
