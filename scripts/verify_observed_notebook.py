#!/usr/bin/env python3
"""Execute and render the authentic metadata-only trajectory without an API call."""
import sys
from verify_notebook import main

if __name__ == '__main__':
    sys.argv.append('--observed')
    main()
