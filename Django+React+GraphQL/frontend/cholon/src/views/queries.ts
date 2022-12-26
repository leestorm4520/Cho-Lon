import gql from 'graphql-tag';

export const PRODUCTS_QUERY = gql`
    query ProductsQuery($search: String) {
        products(search: $search) {
            edges {
                product {
                    id
                    pName
                    pPrice
                    pQuantity
                    pDesc
                }
            }
        }
    }`;

export const PRODUCT_CREATE_MUTATION = gql`
    mutation ProductCreateMutation($input: ProductInputType!) {
        productCreate(input: $input) {
            product {
                id
            }
        }
    }`;

export const PRODUCT_DELETE_MUTATION = gql`
    mutation ProductDeleteMutation($id: ID!) {
        productDelete(id: $id){
            ok
        }
    }`;