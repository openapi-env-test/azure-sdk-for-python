# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.agrifood import AgriFoodMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-agrifood
# USAGE
    python check_name_availability_check_name_availability_available.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AgriFoodMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="11111111-2222-3333-4444-555555555555",
    )

    response = client.check_name_availability.check_name_availability(
        name_availability_request={"name": "newaccountname", "type": "Microsoft.AgFoodPlatform/farmBeats"},
    )
    print(response)


# x-ms-original-file: specification/agrifood/resource-manager/Microsoft.AgFoodPlatform/preview/2023-06-01-preview/examples/CheckNameAvailability_CheckNameAvailability_Available.json
if __name__ == "__main__":
    main()
