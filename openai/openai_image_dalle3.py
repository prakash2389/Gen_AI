from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

prompt = "Generate image of Hulk playing Tennis?"

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)



############ Edits (DALL·E 2 only)

response = client.images.edit(
    model="dall-e-2",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
    n=1,
    size="1024x1024",
)

print(response.data[0].url)


##  Variations (DALL·E 2 only)

response = client.images.create_variation(
    model="dall-e-2",
    image=open("corgi_and_cat_paw.png", "rb"),
    n=1,
    size="1024x1024"
)

print(response.data[0].url)