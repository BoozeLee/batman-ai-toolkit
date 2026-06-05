#!/usr/bin/env python3
"""
Batarang CLI - Batman AI Command Line Interface
Usage: python -m batman_ai.batarang [command]
"""
import sys
import json
from .alfred import AlfredAI
from .batcomputer import BatcomputerCore
from .arsenal import BatArsenal
from .gotham import GothamDB

def main():
    if len(sys.argv) < 2:
        print("🦇 Batarang CLI - Batman AI Toolkit")
        print("Commands: analyze, threats, mission, arsenal, patrol, help")
        return
    
    cmd = sys.argv[1].lower()
    alfred = AlfredAI()
    bc = BatcomputerCore()
    arsenal = BatArsenal()
    gotham = GothamDB()
    
    if cmd == "analyze":
        print(json.dumps(alfred.system_analysis(), indent=2))
    elif cmd == "threats":
        location = sys.argv[2] if len(sys.argv) > 2 else "Gotham"
        threats = bc.analyze_threats(location)
        print(json.dumps(threats, indent=2))
    elif cmd == "mission":
        name = sys.argv[2] if len(sys.argv) > 2 else "New Mission"
        obj = sys.argv[3] if len(sys.argv) > 3 else "Investigate"
        result = bc.start_mission(name, obj)
        print(json.dumps(result, indent=2))
    elif cmd == "arsenal":
        print(json.dumps(arsenal.status(), indent=2))
    elif cmd == "patrol":
        print(json.dumps(gotham.patrol_status(), indent=2))
    elif cmd == "help":
        print("Batarang CLI Commands:")
        print("  analyze          - System analysis")
        print("  threats [loc]    - Threat analysis")
        print("  mission [name]   - Start mission")
        print("  arsenal          - Arsenal status")
        print("  patrol           - Patrol status")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
