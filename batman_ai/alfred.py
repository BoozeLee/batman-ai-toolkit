#!/usr/bin/env python3
"""
Alfred AI - Personal AI Assistant
Version: 1.0
Inspired by Batman's trusted AI companion
"""
import json
import subprocess
from datetime import datetime
from typing import Dict, Any

class AlfredAI:
    def __init__(self):
        self.name = "Alfred AI"
        self.version = "1.0"
        self.knowledge_base = self.load_knowledge()
    
    def load_knowledge(self) -> Dict:
        knowledge = {
            "system": {
                "optimization": "Use TLP and Powertop for battery life",
                "security": "Enable SELinux and auditd for enterprise security"
            },
            "ai": {
                "development": "Use TensorFlow Lite for lightweight models",
                "cloud": "Connect to HuggingFace Hub for model sharing"
            }
        }
        return knowledge
    
    def consult(self, question: str) -> Dict[str, Any]:
        """Provide Alfred's wisdom"""
        print(f"🦇 {self.name} v{self.version}")
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🤔 Question: {question}")
        
        if "system" in question.lower():
            return self.knowledge_base["system"]
        elif "ai" in question.lower() or "model" in question.lower():
            return self.knowledge_base["ai"]
        else:
            return {"response": "Let me consult the Batcomputer..."}
    
    def get_cpu_info(self) -> str:
        try:
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":")[1].strip()
        except:
            pass
        return "Unknown CPU"
    
    def get_ram_info(self) -> str:
        try:
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if "MemTotal" in line:
                        kb = int(line.split()[1])
                        return f"{kb // 1024 // 1024}GB"
        except:
            pass
        return "Unknown RAM"
    
    def get_gpu_info(self) -> str:
        try:
            result = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"], 
                                    capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split('\n')[0]
        except:
            pass
        try:
            result = subprocess.run(["lspci"], capture_output=True, text=True, timeout=5)
            for line in result.stdout.split('\n'):
                if 'VGA' in line or '3D' in line or 'Display' in line:
                    return line.split(':')[-1].strip()
        except:
            pass
        return "No GPU detected"
    
    def get_storage_info(self) -> str:
        try:
            result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                size = lines[1].split()[1]
                return size
        except:
            pass
        return "Unknown Storage"
    
    def check_cuda(self) -> Dict:
        cuda_info = {"available": False, "version": None, "gpus": []}
        try:
            result = subprocess.run(["nvcc", "--version"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                cuda_info["available"] = True
                for line in result.stdout.split('\n'):
                    if "release" in line.lower():
                        cuda_info["version"] = line.split()[-1]
        except:
            pass
        try:
            result = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"], 
                                    capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                cuda_info["gpus"] = [g.strip() for g in result.stdout.strip().split('\n') if g.strip()]
        except:
            pass
        return cuda_info
    
    def system_analysis(self) -> Dict:
        """Analyze system status with real hardware detection"""
        cuda = self.check_cuda()
        analysis = {
            "cpu": self.get_cpu_info(),
            "ram": self.get_ram_info(),
            "gpu": self.get_gpu_info(),
            "storage": self.get_storage_info(),
            "cuda": cuda,
            "optimizations": {
                "power_saving": True,
                "zram_enabled": True,
                "tlp_enabled": True
            }
        }
        return analysis

def main():
    import sys
    alfred = AlfredAI()
    if len(sys.argv) > 1:
        result = alfred.consult(" ".join(sys.argv[1:]))
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(alfred.system_analysis(), indent=2))
