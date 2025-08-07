enum UserRole {
  User = 0,
  Admin = 1,
  Guest = 2
}



let enumUserRole: UserRole = UserRole.User;





// alternative Literal Types



type UserRoleLiteral = 'user' | 'admin' | 'guest';


function getUserRole(role: UserRole): string {
    switch (role) {
        case UserRole.User:
            return 'user';
        case UserRole.Admin:
            return 'admin';
        case UserRole.Guest:
            return 'guest';
        default:
            return 'unknown';
    }
}







function access(role:UserRole): boolean {
    switch (role) {
        case UserRole.Admin:
            return true;
        case UserRole.User:
            return true;
        case UserRole.Guest:
            return false;
        default:
            return false;
    }
}
