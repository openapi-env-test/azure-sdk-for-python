# Azure Purview for Python

> see https://aka.ms/autorest

### Setup

Install Autorest v3

```ps
npm install -g autorest
```

### Generation

```ps
cd <swagger-folder>
autorest
```

### Settings

``` yaml
license-header: MICROSOFT_MIT_NO_VERSION
package-name: azure-purview-administration
no-namespace-folders: true
package-version: 1.0.0b1
version-tolerant: true
```

### Python multi-client

Generate all API versions currently shipped for this package

```yaml
require:
  - https://github.com/Azure/azure-rest-api-specs/blob/9e30496a8803beb5a84909997e5cd7ea0f242fd8/specification/purview/data-plane/readme.md
batch:
  - purview-account: true
  - purview-metadata: true
```

### Tag: package-account

These settings apply only when `--tag=package-account` is specified on the command line.
Please also specify `--python-sdks-folder=<path to the root directory of your azure-sdk-for-python clone>`.

``` yaml $(purview-account)
output-folder: ../azure/purview/administration/account
namespace: azure.purview.administration.account
clear-output-folder: true
title: PurviewAccountClient
add-credential: true
credential-scopes: https://purview.azure.net/.default
```

### Tag: package-metadatapolicies

These settings apply only when `--tag=package-metadatapolicies` is specified on the command line.
Please also specify `--python-sdks-folder=<path to the root directory of your azure-sdk-for-python clone>`.

``` yaml $(purview-metadata)
output-folder: ../azure/purview/administration/metadatapolicies
namespace: azure.purview.administration.metadatapolicies
clear-output-folder: true
title: PurviewMetadataPoliciesClient
add-credential: true
credential-scopes: https://purview.azure.net/.default
```
