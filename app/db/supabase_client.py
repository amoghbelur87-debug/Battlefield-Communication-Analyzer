from supabase import create_client, Client
from app.config import SUPABASE_URL, SUPABASE_KEY

class SupabaseClient:
    def __init__(self):
        self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get_client(self) -> Client:
        return self.client


# Singleton instance (important)
supabase_instance = SupabaseClient().get_client()