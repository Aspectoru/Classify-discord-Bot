import discord
from discord.ext import commands
import os, random
import requests
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(nama_file)
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')
            await ctx.send(f'alamat cloud discord untuk file {url_file}')

            kelas, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')

            if kelas == 'Merpati' and skor >= 0.65:
                await ctx.send("Anda mengirimkan gambar burung merpati")
                await ctx.send(f"Presentase kemiripan yaitu {skor} ")
                #fakta merpati
                await ctx.send("Tahukah? Merpati memiliki kemampuan navigasi yang luar biasa, dapat kembali ke sarang dari jarak ribuan kilometer dengan menggunakan petunjuk seperti medan magnet dan posisi matahari.")


            elif kelas == "Pipit" and skor >=0.65: 
                await ctx.send("Anda mengirimkan gambar burung Pipit")
                await ctx.send(f"Presentase kemiripan yaitu {skor} ")  
                await ctx.send("Tahukah? Burung pipit memiliki kemampuan beradaptasi yang tinggi, dapat hidup di berbagai lingkungan, mulai dari perkotaan hingga pedesaan, dan sering ditemukan di tempat-tempat yang dekat dengan manusia.")


            elif kelas == "Perkutut" and skor >=0.65: 
                await ctx.send("Anda mengirimkan gambar burung Perkutut")
                await ctx.send(f"Presentase kemiripan yaitu {skor} ")    
                await ctx.send("Tahukah? Burung perkutut dikenal dengan suara kicauannya yang merdu, yang sering dianggap membawa keberuntungan dan digunakan dalam berbagai tradisi budaya.")  

            else : 
                await ctx.send("Ini gambar apa bro?")           
    else:
        await ctx.send('Kamu tidak mengirimkan apa apa!')

bot.run("")








