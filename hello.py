import typer,base64 as b
app=typer.Typer()
@app.command()
def main(name:str,lastname:str=typer.Option("",help="Фамилия")):
    print(b.b64decode(b'SGVsbG8gYXBwc2Vjd29ybGQ=').decode()+f" from {name}{' '+lastname if lastname else ''}")
if __name__=="__main__":app()
# test comment
# another comment
