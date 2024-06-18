provider "azurerm" {
  features {}
}

provider "local" {
  version = "~> 2.1"
}

provider "null" {
  version = "~> 3.1"
}

provider "template" {
  version = "~> 2.2"
}
