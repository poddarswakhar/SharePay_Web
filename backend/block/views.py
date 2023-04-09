from django.shortcuts import render
from block.models import Group
from block.serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def grp(request):
    """
    {
	"user1_name": "Jack",
	"user1_wal": "111",
	"user2_name": "John",
	"user2_wal": "222",
	"user3_name": "James",
	"user3_wal": "333",
	"dest_wal": "444",
	"ind_val": 21,
	"serv_name": "Netflix",
	"serv_acc_id": "123123"
}
    """
    if request.method == 'GET':
        data = Group.objects.all()
        serializer = GroupSerializers(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupSerializers(data=request.data)
        if serializer.is_valid():
            n = serializer.data
            try:
                temp_data = Group(user1_name=n['user1_name'], user1_wal=n['user1_wal'], user2_name=n['user2_name'],
                                  user2_wal=n['user2_wal'],
                                  user3_name=n['user3_name'], user3_wal=n['user3_wal'], dest_wal=n["dest_wal"],
                                  ind_val=n["ind_val"], serv_name=n["serv_name"], serv_acc_id=n["serv_acc_id"])
                temp_data.save()
                return Response(status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("INVALID REQUEST!")


@api_view(['DELETE'])
def grp_del(request):
    """
    http://127.0.0.1:8000/api/models/group_del/?pk=2
    """
    try:
        pk = request.query_params.get('pk')
        data = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
