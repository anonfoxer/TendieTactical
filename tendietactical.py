import discord
import random
from discord.ext import commands
import time
import asyncio

client = commands.Bot(command_prefix = '%') #%help, etc
helptext = 'Welcome to TendieTactical\nMade By: anonfoxer\ngithub.com/anonfoxer/TendieTactical\nCommands:\n-----\n- help | displays this text!\n - info | instructs first time users what to do!\n  - setup | sets up all neccissary roles and other bits and bobs for the bot to function!\n - tendies | get tendies!\n - purge | clear a channel of messages!\n - kick | kick a member!\n - ban | ban a member!\n - torture | torture someone with earrape!\n - mute | mute a member!'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('%help'))
    print('Tendie Tactical Unit ready for deployment')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

## @client.event #Member join autoroler
## async def on_member_join(member):
##    print(f'{member} has joined and was given Commoner.')
  ##  role = discord.utils.get(member.server.roles, name='Commoner')
##    await client.add_roles(member, role) Server Specific

permissions = '-Admin Privs\n-Manage Roles\n-Kick & Ban Members\n-Manage Messages'

@client.event #Member loss | || || |_
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send('ポング！')
    print(f'WEEBMODE')

@client.command(pass_context=True)
async def tendies(ctx):
    await ctx.send_file(channel, 'tendies.png')

@client.command(pass_context=True)
async def info(ctx):
    await ctx.send('Welcome to TendieTactical. This bot is written by anonfoxer.')
    await ctx.send('Please make sure that I have the following permissions:')
    await ctx.send(permissions)
    await ctx.send('If I have all of these permissions, then run the setup command!')

@client.command(pass_context=True)
async def setup(ctx):
    await ctx.send('Setting up! This may take a bit, depending on latency!')
    print('setup init')
    author = ctx.message.author
    perms = discord.Permissions(send_messages=False, read_messages=True)
    await client.create_role(author.server, name="Muted", colour=discord.Colour(0xffffff), permissions=perms)
    print('mute role made')

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def torture(ctx, target : discord.Member):
    channel = client.get_channel('521893676147015681') or client.get_channel('577138089386967058')
    print('Bot joined channel')
    await client.move_member(target, channel) #move the target
    vc= await client.join_voice_channel(channel)
    player = vc.create_ffmpeg_player('microwave.mp3', after=lambda: print('done'))
    player.start()
    while not player.is_done():
        await asyncio.sleep(1)
    # disconnect after the player has finished
    player.stop()
    await vc.disconnect()

@client.command(pass_context=True)
async def purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await ctx.send(amount + 'messages purged. Tendie Tactical Unit clearing AO.')



client.run(null)
