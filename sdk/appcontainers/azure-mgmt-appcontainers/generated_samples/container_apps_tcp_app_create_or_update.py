# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.appcontainers import ContainerAppsAPIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python container_apps_tcp_app_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.container_apps.begin_create_or_update(
        resource_group_name="rg",
        container_app_name="testcontainerAppTcp",
        container_app_envelope={
            "location": "East US",
            "properties": {
                "configuration": {
                    "ingress": {
                        "exposedPort": 4000,
                        "external": True,
                        "targetPort": 3000,
                        "traffic": [{"revisionName": "testcontainerAppTcp-ab1234", "weight": 100}],
                        "transport": "tcp",
                    }
                },
                "environmentId": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/rg/providers/Microsoft.App/managedEnvironments/demokube",
                "template": {
                    "containers": [
                        {
                            "image": "repo/testcontainerAppTcp:v1",
                            "name": "testcontainerAppTcp",
                            "probes": [
                                {
                                    "initialDelaySeconds": 3,
                                    "periodSeconds": 3,
                                    "tcpSocket": {"port": 8080},
                                    "type": "Liveness",
                                }
                            ],
                        }
                    ],
                    "scale": {
                        "maxReplicas": 5,
                        "minReplicas": 1,
                        "rules": [{"name": "tcpscalingrule", "tcp": {"metadata": {"concurrentConnections": "50"}}}],
                    },
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/stable/2022-10-01/examples/ContainerApps_TcpApp_CreateOrUpdate.json
if __name__ == "__main__":
    main()
