

import getpass
import os

if not os.environ.get("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")

from langchain.chat_models import init_chat_model

claude_model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")

print(claude_model.invoke("Tell me about coconut industry in india? India is a major imported or exporter?").content)


# The coconut industry in India is significant, and here's a comprehensive overview:
# Production & Status:
# 1. India is one of the leading producers of coconuts globally
# 2. Kerala, Tamil Nadu, Karnataka, and Andhra Pradesh are the major coconut-producing states
# 3. India is the third-largest coconut producer in the world, after Indonesia and the Philippines
# Export-Import Status:
# - Exports:
# 1. India exports coconut products like coconut oil, desiccated coconut, shell charcoal, and coir products
# 2. Major export destinations include UAE, Saudi Arabia, UK, USA, and Kuwait
# - Imports:
# 1. India does import some coconut products, mainly copra and coconut oil
# 2. However, India is generally a net exporter of coconut products
# Key Products:
# 1. Coconut Oil
# 2. Desiccated Coconut
# 3. Coir and Coir products
# 4. Shell charcoal
# 5. Virgin Coconut Oil
# 6. Coconut water
# Industry Support:
# - Coconut Development Board (CDB) under Ministry of Agriculture promotes coconut cultivation and industry development
# - Various schemes and initiatives to support farmers and processors
# While India produces significant quantities of coconuts, it both exports and imports different coconut products based on market demand and prices. Overall, India is more of an exporter than an importer in the coconut industry.
