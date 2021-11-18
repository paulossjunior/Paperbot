from discord.ext import commands
import csv
import codecs

class YellowPagesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print ("Fufando")

    @commands.command(help='retrive all papers by a word in title or name of author')
    async def find(self, ctx, arg):
        notFound = True
        csv_reader = csv.reader(codecs.open('yellowpages.csv', 'rU', 'utf-16'), delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
             
            title = row[0]
            title = title.lower()
            title_result = title.find(arg.lower())

            author = row[1]
            author = author.lower()
            author_result = author.find(arg.lower())

            if author_result != -1 or title_result != -1:
                notFound = False
                message = "- *"+row[0].strip()+"* - "+row[1].strip()+" - "+row[2].strip()
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
    client = YellowPages("OTEwODU2ODM2MjQ3MzI2Nzgx.YZY7iA.Bdcfgf9eQdlVZzXrDkA5AxCc7wk")
