import os, datetime

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.management import call_command
from django.core.exceptions import ValidationError

from .permissions import IsStaffOrReadOnly

pfad = "/app/backups/"

class BackupGetPostView(APIView):    
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

    def get(self, request, *args, **kwargs):    
        backups = os.listdir(pfad)

        return Response({
            'backups': backups,
        })
        
    def post(self, request, *args, **kwargs):
        x = datetime.datetime.now()
        backup_filename = "backup_" + x.strftime("%Y%m%d_%H:%M:%S") + ".json"
        voller_pfad = pfad + backup_filename
       
        with open(voller_pfad, "w") as f:
            call_command("dumpdata", exclude=["contenttypes", "auth", "allauth", "sessions"], stdout=f,)
        
        msg = f"Backup {backup_filename} wurde erfolgreich erstellt!"
        backups = os.listdir(pfad)  
        
        return Response({
            'msg': msg,
            'backups': backups,
        })

class RestorePostView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

    def post(self, request, *args, **kwargs): 
        msg = ""
        backupname = request.data['backup']
        backups = os.listdir(pfad)
        if backupname in backups:
            datei = pfad + backupname
            call_command("loaddata", datei, "--delete")
            name = backupname.split(".")
            name = name[0]
            
            msg = f"Backup {name} wurde erfolgreich importiert!"
        else:
            raise ValidationError(f"Backup nicht gefunden: {backupname}")

        return Response({
            'msg': msg,
            'backups': backups,
        })
