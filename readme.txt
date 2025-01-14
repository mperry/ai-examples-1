
Download Ollama for Windows, see https://www.ollama.com/.
Download the Tiny Llama model by running "ollama pull tinyllama", then "ollama run tinyllama"

To install the Python packages required, run "pip install -r requirements.txt".
To freeze the libraries run "pip freeze >requirements.txt".
To update a lib "pip install <package> -U"

When running pip install, you can get an error like:

      ..\meson.build:1:0: ERROR: Could not find C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe

      A full log can be found at C:\Users\maper\AppData\Local\Temp\pip-install-_kr2kxwf\contourpy_102fb266fc334302bc4bf20eebc7f99b\.mesonpy-jqn1h2fn\meson-logs\meson-log.txt
      [end of output]

To get VS Where directly, go to:
Download it from https://github.com/Microsoft/vswhere/releases
Download VS Studio from https://visualstudio.microsoft.com/downloads/
Install the core C/C++ compilers as per the instructions at https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170

You need Python 3.13.0, not 3.13.1 or above.
I then needed to upgrade pip using the command: "python -m pip install --upgrade pip"

https://rustup.rs/

Collecting jiter==0.4.2 (from -r requirements.txt (line 74))
  Using cached jiter-0.4.2.tar.gz (159 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [6 lines of output]

      Cargo, the Rust package manager, is not installed or is not on PATH.
      This package requires Rust and Cargo to compile extensions. Install it through
      the system's package manager or via https://rustup.rs/

      Checking for Rust toolchain....
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.


Models:
TinyLlama
Llama3

python -m venv venv
