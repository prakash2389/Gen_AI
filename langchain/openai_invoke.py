import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")

print(model.invoke("Tell me about coconut industry in india? India is a major imported or exporter?").content)

# The coconut industry in India is a significant sector within the agricultural economy, playing a vital role in the livelihoods of millions of farmers and contributing to various agro-based industries. India is one of the largest producers of coconuts in the world, along with Indonesia and the Philippines.
# ### Key Aspects of the Coconut Industry in India:
# 1. **Production**: India produces around 15 billion coconuts annually, with major producing states including Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, and West Bengal. Kerala is the largest producer, contributing nearly 45% of the total production. 
# 2. **Varieties and Uses**: The coconut is valued for its various products, including copra (dried coconut), coconut oil, coconut water, tender coconuts, and coir (a natural fiber extracted from the husk of coconuts), which is used in various applications ranging from mats to geotextiles.
# 3. **Economical Importance**: The coconut industry provides employment and supports the rural economy. It offers various opportunities, from farming to processing, and contributes to the export sector.
# 4. **Exports**: India is a significant exporter of coconut products, particularly copra, virgin coconut oil, coconut water, coir products, and desiccated coconut. The primary export markets include the Middle East, the USA, Europe, and Southeast Asia.
# 5. **Challenges**: The industry faces challenges such as fluctuating prices, climate change impacts, pests and diseases, and competition from synthetic substitutes and other edible oils. The need for modernization, quality improvement, and infrastructure development is also essential to sustain growth.
# 6. **Government Initiatives**: The Indian government has implemented various schemes to promote coconut cultivation and processing, including financial assistance, research and development support, and marketing initiatives. Organizations like the Coconut Development Board work towards the development of the industry, providing support to farmers and entrepreneurs.
# ### Conclusion
# In summary, India is primarily a coconut producer and exporter rather than an importer. The coconut industry is crucial for the economy, providing livelihoods and contributing to export earnings. While there are challenges, ongoing efforts by the government and stakeholders aim to enhance productivity and expand market access.

