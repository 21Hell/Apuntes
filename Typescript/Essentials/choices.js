var UserRole;
(function (UserRole) {
    UserRole[UserRole["User"] = 0] = "User";
    UserRole[UserRole["Admin"] = 1] = "Admin";
    UserRole[UserRole["Guest"] = 2] = "Guest";
})(UserRole || (UserRole = {}));
var enumUserRole = UserRole.User;
// alternative Literal Types
var literalUserRole = 'admin';
literalUserRole = 'user';
var posibleResults = [1, -1];
posibleResults = [-1, 2];
console.log(posibleResults);
