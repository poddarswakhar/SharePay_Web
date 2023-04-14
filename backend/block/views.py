from django.shortcuts import render
from block.serializers import *
import time
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings

from utils.functions import deploy_contract, deposit, withdraw

from .models import Group

from datetime import datetime, timedelta


def sendEmail(address, contractAdd):
    send_mail(
        "[Action Needed] SharePay Sign Your Smart Contract Here",
        "Dear User,\n \nYou were added to a group with Smart Contract Address: " + contractAdd + ". Please Sign this contract on www.sharepay.com & click the SIGN CONTRACT button. Thank you.\n"
        + "\nSincerely\nSharePay Admin",
        settings.EMAIL_HOST_USER,
        address,
        fail_silently=False
    )


def sendEmailRenewal(address, contractAdd):
    send_mail(
        "[Action Needed] SharePay Sign Your Renewal Here",
        "Dear User,\n \nYou were set to renew your subscription of Smart Contract Address: " + contractAdd + ". Please Sign this contract on www.sharepay.com & click the SIGN CONTRACT button. Thank you.\n"
        + "\nSincerely\nSharePay Admin",
        settings.EMAIL_HOST_USER,
        address,
        fail_silently=False
    )


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
	"serv_acc_id": "123123",
	"ren": "2023-04-01T03:03:00"
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
                contract_address, abi = deploy_contract()

                while True:
                    # Check the condition
                    if contract_address and abi:
                        # Exit the loop if the condition is true
                        break

                    # Call the sleep function
                    time.sleep(1)

                temp_data = Group(user1_name=n['user1_name'], user1_wal=n['user1_wal'], user2_name=n['user2_name'],
                                  user2_wal=n['user2_wal'],
                                  user3_name=n['user3_name'], user3_wal=n['user3_wal'], dest_wal=n["dest_wal"],
                                  ind_val=n["ind_val"], serv_name=n["serv_name"], serv_acc_id=n["serv_acc_id"],
                                  ren=n["ren"], contract_address=contract_address, abi=abi)
                temp_data.save()

                # deploy thr contract (pass the email list, and from that method call the email(address, contractAddress))
                # for test below line, delete once the deploy function is created and chaining is done
                sendEmail([n['user1_name'], n['user2_name'], n['user3_name']], contract_address)

                return Response(status=status.HTTP_201_CREATED)

            except Exception as e:
                print(e)
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


@api_view(['GET', 'POST'])
def sign(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        public_key = request.query_params.get('pub')
        private_key = request.query_params.get('pri')
        contract_address = request.query_params.get('con')

        group = Group.objects.filter(contract_address=contract_address)

        for a in group:
            abi = a.abi

        if not deposit(public_key, private_key, contract_address, abi):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        st = withdraw(contract_address, abi)

        while True:
            # Check the condition
            if st:
                # Exit the loop if the condition is true
                if st != 1:
                    break

            # Call the sleep function
            time.sleep(1)

        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def anni(request):
    if request.method == 'GET':
        date_string = request.query_params.get('pub')
        date_time_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')

        # start_date = datetime(2020, 1, 1)
        # Subtract 60 seconds
        upper_date = date_time_obj + timedelta(days=30)

        groups = Group.objects.filter(ren__gte=date_time_obj).filter(ren__lt=upper_date)

        serializer = GroupSerializers(groups, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        date_string = request.query_params.get('pub')
        print(date_string.rsplit(":", 1)[0])
        date_time_obj = datetime.strptime(date_string.rsplit(":", 1)[0] + "Z", '%Y-%m-%dT%H:%MZ')

        date_time_obj = date_time_obj - timedelta(hours=8)

        # Subtract 60 seconds
        upper_date = date_time_obj + timedelta(days=1)

        group = Group.objects.filter(ren__gte=date_time_obj, ren__lt=upper_date)

        group_data = GroupSerializers(group, many=True).data

        for elem in group_data:
            sendEmailRenewal([elem['user1_name'], elem['user2_name'], elem['user3_name']], '0xffg123232')

        return Response(status=status.HTTP_202_ACCEPTED)
