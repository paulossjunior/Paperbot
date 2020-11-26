from discord.ext import commands
import discord
import csv

class YellowPagesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print ("Fufando")

    @commands.command(help='retrive all papers by a word in abstract or name of author')
    async def find(self, ctx, arg):
        notFound = True
        with open('yellowpages.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                abstract = row[0]
                abstract = abstract.lower()
                abstract_result = abstract.find(arg.lower())

                title = row[1]
                title = title.lower()
                title_result = title.find(arg.lower())

                author = row[2]
                author = author.lower()
                author_result = author.find(arg.lower())

                if abstract_result != -1 or author_result != -1 or title_result != -1:
                    notFound = False
                    message = "- *"+row[1].strip()+"* - "+row[2].strip()+" - "+row[3].strip()
                    await ctx.send(str(message))
                    
                
        if notFound:
            message = "Nothing found! :("
            await ctx.send(str(message))
    


    @commands.command(help='retrive all papers by a word in abstract')
    async def find_by_word(self, ctx, arg):
        notFound = True
        with open('yellowpages.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                abstract = row[0]
                abstract = abstract.lower()
                result = abstract.find(arg.lower())
                if result != -1:
                    notFound = False
                    message = "- *"+row[1].strip()+"* - "+row[2].strip()+" - "+row[3].strip()
                    await ctx.send(str(message))
                
                
        if notFound:
            message = "Nothing found! :("
            await ctx.send(str(message))
        
        

    @commands.command(help='retrive all papers by an author')
    async def find_by_author(self, ctx, arg):
        notFound = True
        with open('yellowpages.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                author = row[2]
                author = author.lower()
                result = author.find(arg.lower())
                if result != -1:
                    notFound = False
                    message = "- *"+row[1].strip()+"* - "+row[2].strip()+" - "+row[3].strip()
                    await ctx.send(str(message))
                
        if notFound:
            message = "Nothing found! :("
            await ctx.send(str(message))        
    
class YellowPages():

    def __init__(self, token):
        
        self.bot = commands.Bot(command_prefix='$')
        self.bot.add_cog(YellowPagesCommands(self.bot))
        self.bot.run(token)     
    
if __name__ == '__main__':        
    client = YellowPages("seu token")
