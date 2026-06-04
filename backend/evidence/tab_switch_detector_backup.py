"""
Tab Switch Detector Backup Module for Evidence Storage
Records and stores tab switch detection evidence during exam sessions
"""

import time
import json
from typing import List, Dict
from datetime import datetime
from pathlib import Path


class TabSwitchDetectorBackup:
    """Backup tab switch detector for storing evidence"""
    
    def __init__(self, evidence_dir: str = "backend/evidence"):
        self.tab_switches = []
        self.start_time = None
        self.monitoring = False
        self.evidence_dir = Path(evidence_dir)
        self.evidence_dir.mkdir(parents=True, exist_ok=True)
        
    def start_monitoring(self):
        """Start monitoring for tab switches"""
        self.monitoring = True
        self.start_time = time.time()
        self.tab_switches = []
        
    def stop_monitoring(self):
        """Stop monitoring for tab switches"""
        self.monitoring = False
        
    def detect_tab_switch(self, student_id: str = None, trigger_source: str = "focus_loss"):
        """Detect and log a tab switch event"""
        if not self.monitoring:
            return
            
        switch_event = {
            'timestamp': datetime.now().isoformat(),
            'time_since_start': time.time() - self.start_time,
            'trigger_source': trigger_source,
            'student_id': student_id
        }
        self.tab_switches.append(switch_event)
            
    def get_tab_switches(self) -> List[Dict]:
        """Get all recorded tab switches"""
        return self.tab_switches
    
    def get_switch_count(self) -> int:
        """Get total number of tab switches"""
        return len(self.tab_switches)
    
    def save_evidence(self, student_id: str, filename: str = None):
        """Save tab switch evidence to file"""
        if filename is None:
            filename = f"tab_switch_evidence_{student_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        filepath = self.evidence_dir / filename
        evidence_data = {
            'student_id': student_id,
            'detection_start': self.start_time,
            'total_switches': len(self.tab_switches),
            'switches': self.tab_switches,
            'saved_at': datetime.now().isoformat()
        }
        
        with open(filepath, 'w') as f:
            json.dump(evidence_data, f, indent=2)
            
        return str(filepath)
    
    def reset(self):
        """Reset tab switch log"""
        self.tab_switches = []


if __name__ == "__main__":
    detector = TabSwitchDetectorBackup()
