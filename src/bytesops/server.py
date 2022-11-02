from fastapi import FastAPI, UploadFile
import os
"""
Run server to send audio && video as bytes

uvicorn server:app --reload
"""

app = FastAPI()

rootpath = r"C:\Users\codenamewei\Downloads\temp"


@app.put("/multimedia")
async def upload_video(multimedia: UploadFile):
    """
    save video in the current function loop and return response once done
    """
    contents = await multimedia.read()
    outfilepath = os.path.join(rootpath, multimedia.filename)

    if(os.path.exists(outfilepath)):

        os.remove(outfilepath)

    with open(outfilepath, "wb") as fp:
        fp.write(contents)

    print(f"Wrote to file {outfilepath}")

    return dict(success=True, filepath=outfilepath)
