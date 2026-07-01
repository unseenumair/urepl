"""
Native Tab REPL (urepl)
A lightweight, zero-dependency alternative configuration for the standard 
interactive Python shell featuring cross-platform tab completion.

Author: Umair Shakoor
Email: umairshakoor.pro@gmail.com
Repository: https://github.com/unseenumair/urepl
"""

import code
import os
import sys
import getpass

def start_repl():
    """
    Initializes and launches the customized cross-platform interactive REPL session.
    Configures native autocompletion dynamically based on the host operating system.
    """
    
    # -------------------------------------------------------------------------
    # 1. CROSS-PLATFORM TAB COMPLETION CONFIGURATION
    # -------------------------------------------------------------------------
    # We attempt to bind native readline first (Unix/macOS). If that fails, we fallback 
    # to pyreadline3 (Windows). If both fail, the REPL gracefully loads without completion.
    try:
        # Standard configuration for Unix-based systems (Linux, macOS)
        import readline
        import rlcompleter
        readline.parse_and_bind("tab: complete")
        readline.set_completer(rlcompleter.Completer(globals()).complete)
        
    except ImportError:
        try:
            # Fallback configuration for Windows environments
            import pyreadline3 as windows_readline
            import rlcompleter
            windows_readline.parse_and_bind("tab: complete")
            windows_readline.set_completer(rlcompleter.Completer(globals()).complete)
            
        except ImportError:
            # Safe degradation if no completion libraries are locally present
            pass

    # -------------------------------------------------------------------------
    # 2. DYNAMIC ENVIRONMENT BANNER GENERATION
    # -------------------------------------------------------------------------
    current_username = getpass.getuser().upper()
    operating_system = sys.platform.lower()
    
    # Safely retrieve machine network node name across differing OS kernel systems
    if hasattr(os, 'uname'):
        network_hostname = os.uname().nodename.lower()
    else:
        network_hostname = os.environ.get('COMPUTERNAME', 'unknown').lower()

    session_greeting_banner = f"WhatsUp, {current_username} on {operating_system}@{network_hostname}"

    # -------------------------------------------------------------------------
    # 3. INTERACTIVE CONSOLE SETTINGS & RUNTIME LAUNCH
    # -------------------------------------------------------------------------
    # Overriding the primary string prompt indicator
    sys.ps1 = "python >> "

    # Passing globals() allows the REPL to retain access to imported scripts 
    # and custom local variables perfectly during execution loops.
    interactive_session = code.InteractiveConsole(locals=globals())
    
    interactive_session.interact(
        banner=session_greeting_banner,
        exitmsg="Built by UMAIR"
    )

if __name__ == "__main__":
    start_repl()
