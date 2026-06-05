#!/usr/bin/env python3
"""
Bat-Arc Reactor & Arsenal Management
"""
import json
from datetime import datetime
from typing import Dict, List

class BatArsenal:
    def __init__(self):
        self.name = "Bat-Arsenal"
        self.version = "1.0"
        self.equipment = {
            "tools": [
                {"name": "Batarang", "type": "utility", "status": "ready"},
                {"name": "Grappling Hook", "type": "mobility", "status": "ready"},
                {"name": "Utility Belt", "type": "container", "status": "ready"},
                {"name": "Detective Mode", "type": "sensor", "status": "ready"},
                {"name": "Cape", "type": "mobility", "status": "ready"}
            ],
            "weapons": [
                {"name": "Batarang", "type": "throwable", "ammo": 100},
                {"name": "Foam Pellets", "type": "non-lethal", "ammo": 50}
            ]
        }
    
    def status(self) -> Dict:
        return {
            "arsenal": self.name,
            "version": self.version,
            "last_update": datetime.now().isoformat(),
            "total_items": len(self.equipment["tools"]) + len(self.equipment["weapons"])
        }
    
    def deploy(self, item: str) -> str:
        for tool in self.equipment["tools"]:
            if tool["name"].lower() == item.lower():
                return f"Deploying {item} - {tool['type']} ready"
        return f"Item '{item}' not found in arsenal"

def main():
    import sys
    arsenal = BatArsenal()
    if len(sys.argv) > 1:
        print(arsenal.deploy(sys.argv[1]))
    else:
        print(json.dumps(arsenal.status(), indent=2))

if __name__ == "__main__":
    main()
