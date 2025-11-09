import os

try:
   import streamlit as st
except Exception:
   st = None


def get_secret(name, default=None):
   """Get a secret either from Streamlit secrets (when deployed) or from environment variables (.env locally).
   Usage: get_secret("NEWSAPI_KEY")
   """
   # Streamlit Cloud / secrets
   try:
      if st is not None and hasattr(st, "secrets") and name in st.secrets:
         return st.secrets[name]
   except Exception:
      pass
   return os.getenv(name, default)