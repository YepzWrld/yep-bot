import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=";")
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game("Watching Over YepzWrld Productions! (;)"))
	print("Bot is ready")

@client.command()
async def ping(ctx):
	await ctx.send("pong")

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {user.mention}')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {user.mention}')

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=5):
	 await ctx.channel.purge(limit=amount)

@client.command()
async def rob(ctx):
	await ctx.send("Your a Bad Person! You just Robbed them!")

@client.command()
async def arrest(ctx):
	await ctx.send("Don't worry We got him! :rotating_light:")

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

@client.command(invoke_without_command=True)
async def help(ctx):
	em = discord.Embed(title = "Help", description = "**Use the Ticket bot for more questions!**", colour = ctx.author.colour)

	em.add_field(name = "Moderation", value = "Kick,Ban,Unban,Clear")
	em.add_field(name= "Fun", value = "Arrest,rob")


	await ctx.send(embed = em)

@client.command(aliases=['8ball', '8b'])
async def eightball(ctx, *, question):
	responses = ["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."]
	await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}')

client.run("ODA5NzQ0ODIyMzMxMjQ0NTk0.YCZjoQ.7i5pQsCMmMkp-e5gk0U8Mdq4bF8")