#!/bin/bash

# Variables (modifiez-les selon vos besoins)
RESOURCE_GROUP="votre-resource-group"
VM_NAME="votre-vm-name"

# Se connecter à Azure (assurez-vous d'utiliser les bonnes méthodes d'authentification)
az login --identity

# Arrêter la VM
az vm stop --resource-group $RESOURCE_GROUP --name $VM_NAME

# Désallouer la VM
az vm deallocate --resource-group $RESOURCE_GROUP --name $VM_NAME

echo "VM $VM_NAME in resource group $RESOURCE_GROUP has been stopped and deallocated."
