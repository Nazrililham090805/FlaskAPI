from flask import Blueprint, jsonify, request
from services.service import delete_store_by_Store_name_service, add_store_service

store_blueprint = Blueprint('Store', __name__)

@store_blueprint.route('/api/store/<store_name>', methods=['DELETE'])
def delete_store_by_Store_name(store_name):  
    success, error_msg = delete_store_by_Store_name_service(store_name)
    if success:
        return jsonify({'message': 'Store deleted successfully'}), 200
    else:
        return jsonify({'message': 'Error deleting store', 'error': error_msg}), 500

@store_blueprint.route('/api/add_store', methods=['POST']) 
def add_store():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Customer name, Book name, Description, and rating is required'})
    
    store_name = data.get('store_name')
    email = data.get('email')
    phone = data.get('phone')
    address_id = data.get('address_id')
    success, error_msg = add_store_service(store_name, email, phone, address_id)
    if success:
        return jsonify({'message': 'Review updated successfully'}), 200
    else:
        return jsonify({'message': 'Error updating review book', 'error': error_msg}), 500   