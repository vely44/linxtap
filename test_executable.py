#!/usr/bin/env python3
"""
Test script to verify the executable can start and initialize properly.
This creates a minimal Qt application that starts and immediately exits.
"""

import sys
import os
import subprocess
import time

def test_executable():
    """Test that the executable can be launched"""
    executable_path = "dist/LinxTap/LinxTap"

    if not os.path.exists(executable_path):
        print(f"❌ Executable not found at {executable_path}")
        return False

    print(f"✓ Executable found at {executable_path}")
    print(f"  Size: {os.path.getsize(executable_path) / 1024 / 1024:.2f} MB")

    # Check if executable is executable
    if not os.access(executable_path, os.X_OK):
        print(f"❌ File is not executable")
        return False

    print("✓ File has executable permissions")

    # Try to run the executable (it will time out since it's a GUI app)
    print("\nTrying to launch the executable...")
    env = os.environ.copy()
    env['QT_QPA_PLATFORM'] = 'offscreen'

    try:
        proc = subprocess.Popen(
            [f"./{executable_path}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            text=True
        )

        # Wait a bit to see if it starts
        time.sleep(2)

        # Check if process is still running
        if proc.poll() is None:
            print("✓ Executable started successfully!")
            print("  Process is running (PID: {})".format(proc.pid))

            # Kill the process
            proc.terminate()
            proc.wait(timeout=5)
            print("✓ Executable terminated cleanly")
            return True
        else:
            stdout, stderr = proc.communicate()
            print(f"❌ Executable exited with code {proc.returncode}")
            if stderr:
                print(f"  Error: {stderr[:200]}")
            return False

    except subprocess.TimeoutExpired:
        print("✓ Executable is running (timeout reached)")
        proc.kill()
        return True
    except Exception as e:
        print(f"❌ Error running executable: {e}")
        return False

if __name__ == "__main__":
    print("Testing LinxTap Executable")
    print("=" * 50)
    success = test_executable()
    print("=" * 50)
    if success:
        print("\n✓ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Tests failed!")
        sys.exit(1)
