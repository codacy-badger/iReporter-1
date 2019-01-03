from flask import request, jsonify
from api.redflags.models import RedFlag, BaseRedFlag
from db.database import RedflagsDb

redflags = RedflagsDb()


class RedFlagsController:

    def create_redflag(self):
        
        data = request.get_json()

        title = data.get('title')
        redflagType = data.get('redflagType')
        location = data.get('location')
        status = data.get('status')
        image = data.get('image')
        video = data.get('video')
        comment = data.get('comment')

        redflag = RedFlag(BaseRedFlag(status, image, video, comment),
                          title, redflagType, location)
        
        redflags.add_redflag(redflag)
        return jsonify({
            "status": 201,
            "message": "Redflag successfully created.",
            "data": redflag.to_json
        }), 201

    def fetch_all_redflags(self):
        all_redflags = [i.to_json for i in redflags.get_all_redflags()]
        return jsonify({
            "status": 200,
            "message": "success",
            "Redflags": all_redflags
        }), 200